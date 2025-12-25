# Organization Agent & Skill Architecture

**Last Updated:** 2025-12-25
**Status:** Active Documentation

## Overview

This organization operates as an **AI-first business** where the workforce is composed primarily of AI agents. This document describes the current architecture of agents, skills, and organizational systems.

---

## Directory Structure

```
aphebis-world-builder-claude/
├── .claude/
│   ├── agents/           # Autonomous agent definitions
│   │   ├── business-manager.md
│   │   ├── technical-strategy-advisor.md
│   │   └── docs-query-expert.md
│   │
│   └── skills/           # Reusable skill definitions (invocable)
│       ├── pso/          # Project Support Officer
│       └── magnus-the-world-builder/
│
├── skills/               # Skill symlink/backup directory
│   └── pso/
│
└── org/                  # Organizational data & projects
    ├── engineering/      # Engineering documentation (this file)
    └── projects/         # Project artifacts managed by PSO
        ├── project-list.csv
        ├── project-activity-logs.csv
        └── {id}-{name}/
```

---

## Agents vs. Skills

| Aspect | Agents | Skills |
|--------|--------|--------|
| **Purpose** | Autonomous, goal-oriented specialists | Reusable capabilities invoked by name |
| **Invocation** | Launched via Task tool | Invoked via Skill tool or `/skillname` |
| **State** | Maintains conversation context | Stateless, fresh invocation |
| **Use Case** | Complex multi-step tasks, research, decisions | Standardized operations, data access |
| **Examples** | business-manager, technical-strategy-advisor | pso, magnus-the-world-builder |

### When to Use Which

- **Use an Agent** when you need:
  - Strategic thinking or decision-making
  - Complex multi-step workflows
  - Research and analysis
  - Autonomous operation with context

- **Use a Skill** when you need:
  - Standardized data access (e.g., project lookup)
  - Repeatable operations (e.g., create project)
  - Structured workflows with clear inputs/outputs
  - Integration with external systems

---

## Current Agent Roster

### Executive Layer

| Agent | ID | Model | Purpose |
|-------|-----|-------|---------|
| **Business Manager** | `business-manager` | Opus | Strategic business guidance, decision-making, resource allocation, risk assessment |
| **Technical Strategy Advisor** | `technical-strategy-advisor` | Opus | High-level technical guidance, architectural decisions, compliance evaluation |

### Specialist Layer

| Agent | ID | Model | Purpose |
|-------|-----|-------|---------|
| **Docs Query Expert** | `docs-query-expert` | Haiku | Documentation research, grounding answers in official docs |

---

## Current Skill Roster

| Skill | Purpose | Key Operations |
|-------|---------|----------------|
| **pso** (Project Support Officer) | Project and artifact management | Create/query/update projects, record activity, manage artifacts |
| **magnus-the-world-builder** | World-building for Aphebis platform | Browse/create worlds, areas, locations; narrative development |

---

## Agent Definition Format

Agents are defined as Markdown files with YAML frontmatter in `.claude/agents/`:

```yaml
---
name: agent-id
description: When to use this agent, with examples
model: opus|sonnet|haiku
color: display-color
tools: comma,separated,tool,list
---

# Agent Name

Free-form agent instructions and behavior definition...
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique agent identifier (kebab-case) |
| `description` | Yes | Usage guidance with examples for the main Claude to reference |
| `model` | No | Model to use (defaults to configured model) |
| `color` | No | Display color in UI |
| `tools` | No | MCP tools available to this agent |

### Agent Instructions Body

The main content defines:
- Core identity and responsibilities
- Operational approach and frameworks
- Communication style
- Quality assurance practices
- When to escalate or delegate
- Output format expectations

---

## Skill Definition Format

Skills are defined as Markdown files with YAML frontmatter in `.claude/skills/{skill-name}/`:

```yaml
---
name: skill-id
description: When to invoke this skill
---

# Skill Name

Instructions for how to operate this skill, including:
- Data structures used
- Available scripts/operations
- Usage workflows
- Error handling
- Scope boundaries
```

### Skills with Scripts

Some skills (like PSO) include executable scripts:

```
.claude/skills/{skill-name}/
├── SKILL.md              # Skill definition
├── scripts/              # Python scripts
│   ├── utils.py          # Shared utilities
│   ├── operation1.py
│   └── operation2.py
└── org/                  # Skill-managed data
    └── ...
```

---

## The PSO Skill: A Reference Architecture

The Project Support Officer (PSO) serves as a reference implementation for data-managing skills.

### Data Model

```csv
# org/projects/project-list.csv
projectId,projectName,description,startDate,endDate

# org/projects/project-activity-logs.csv
projectId,datetime,agentName,note
```

### Script Pattern

Each PSO script:
1. Imports shared utilities (`pso_utils.py`)
2. Ensures directories exist
3. Reads/writes CSV files atomically
4. Returns JSON output
5. Requires caller identification (`--agent-name`)

### Permission Model

PSO implements role-based access control:
- All operations require agent identification
- Project closure requires "project manager" role verification
- All actions are logged to activity logs

---

## Organizational Systems

### Project Management (via PSO)

- **Projects** are tracked in `org/projects/project-list.csv`
- Each project has a unique 6-character ID
- Active projects have empty `endDate`
- Artifacts are stored in `org/projects/{id}-{sanitized-name}/`

### Activity Logging

- All project-related actions are logged
- Logs include: project ID, timestamp, agent name, activity note
- Enables audit trail and activity analysis

### Engineering Documentation

- Architecture docs live in `org/engineering/`
- This document is the starting point
- As the org grows, add: API docs, runbooks, decision records

---

## Naming Conventions

| Type | Convention | Examples |
|------|------------|----------|
| Agent IDs | `kebab-case` | `business-manager`, `technical-strategy-advisor` |
| Skill IDs | `kebab-case` | `pso`, `magnus-the-world-builder` |
| Project IDs | 6-char alphanumeric | `eyH0pG`, `ABC123` |
| Project folders | `{id}-{kebab-name}` | `eyH0pG-business-manager-agent` |
| CSV files | `kebab-case.csv` | `project-list.csv` |

---

## Creating New Agents

When adding a new agent:

1. Create `.claude/agents/{agent-name}.md`
2. Include comprehensive description with usage examples
3. Specify model and tools if needed
4. Define clear scope and boundaries
5. Document escalation criteria
6. Test agent behavior in varied scenarios

### Agent Design Checklist

- [ ] Clear purpose and use cases
- [ ] Appropriate model selection (Opus for complex, Haiku for fast/cheap)
- [ ] Tool access defined (if MCP tools needed)
- [ ] Behavioral boundaries set
- [ ] Output format specified
- [ ] Escalation paths defined

---

## Creating New Skills

When adding a new skill:

1. Create `.claude/skills/{skill-name}/SKILL.md`
2. Define operation contracts (inputs/outputs)
3. If using scripts: add `scripts/` folder with utilities
4. If managing data: define data structures and storage
5. Implement error handling
6. Document scope boundaries

### Skill Design Checklist

- [ ] Clear trigger conditions in description
- [ ] Stateless or explicit state management
- [ ] Idempotent operations where possible
- [ ] Error handling defined
- [ ] Scope clearly bounded
- [ ] Documentation includes examples

---

## Integration Patterns

### Agent-to-Skill

Agents can invoke skills:
- Business Manager may invoke PSO to create a project for a new initiative
- Any agent may invoke magnus-the-world-builder for narrative work

### Agent-to-Agent

Agents can launch other agents:
- Business Manager may launch Technical Strategy Advisor for architecture decisions
- Any agent may launch Docs Query Expert for research

### Skill-to-Skill

Skills typically don't invoke other skills (keep it simple).

---

## Open Questions & Future Considerations

1. **Org Chart:** Should there be a canonical org chart file? Currently implicit.
2. **Agent Permissions:** No central permission system yet (PSO has its own).
3. **Discovery:** How will agents discover available skills/agents dynamically?
4. **Versioning:** No versioning for agent/skill definitions yet.
5. **Testing:** No automated testing framework for agent behaviors.
6. **Monitoring:** No observability into agent invocation patterns.

---

## Engineering Gaps

As of 2025-12-25, the following roles are unfilled:

| Role | Description | Priority |
|------|-------------|----------|
| **Engineering Manager** | Would own this doc, coordinate technical hiring, manage tech debt | High |
| **DevOps/SRE** | Infrastructure, monitoring, deployment, reliability | Medium |
| **QA/Testing** | Agent/skill testing framework, validation | Medium |
| **Security Officer** | Security review, compliance, access control | High |

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2025-12-25 | Initial architecture documentation | Claude |
