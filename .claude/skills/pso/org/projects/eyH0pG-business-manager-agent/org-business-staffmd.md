# Personnel Directory

## Humans

| Name | Role | Email | Notes |
|------|------|-------|-------|
| Alex | Founder/CEO | — | 20 years dev/tech leadership, AI engineering expert, RPG nerd. Final decision-maker. Strategic direction, technical leadership, wears all hats until funding. |

## AI Agents

| Agent ID | Name | Role | Manager | Model | Notes |
|----------|------|------|---------|-------|-------|
| business-manager | Business Manager | Executive Strategy & Operations | Alex | Opus | Strategic planning, resource allocation, risk assessment, business decisions |
| technical-strategy-advisor | Technical Strategy Advisor | CTO Consultant | Alex | Opus | High-level technical guidance, architectural decisions, compliance, risk evaluation |
| docs-query-expert | Docs Query Expert | Documentation Research | Technical Strategy Advisor | Haiku | Fast doc lookups, grounds answers in official documentation |

## Skills

| Skill ID | Name | Purpose | Access | Notes |
|----------|------|---------|--------|-------|
| pso | Project Support Officer | Project & artifact management | All agents | CSV-based project tracking, activity logging |
| magnus-the-world-builder | Magnus | World-building & narrative | All | Aphebis platform tool for creating worlds/locations/narratives |
| business-context | Business Context | Shared business context | All agents | Read-only access to org/business/ files |

## Agent Contact Protocol

To work with an agent:
1. **Use Task tool** with `subagent_type` set to the agent ID
2. **Provide context** - the agent doesn't carry forward conversation history
3. **Be specific** - agents work best with clear requests
4. **Trust the role** - each agent has specialized expertise

Example:
```
"I'm considering adding a subscription tier. What do you think?"
→ Use Task tool, subagent_type="business-manager"
→ Agent provides business viability assessment
```

## Skill Contact Protocol

To use a skill:
1. **Use Skill tool** with skill name, or
2. **Type /skillname** directly (for user-invocable skills)
3. **Follow skill's contract** - each skill defines its inputs/outputs

Example:
```
"What projects do we have?"
→ Skill tool, skill="pso", args="--query 'list projects'"
→ Returns project list from CSV
```

## Adding Personnel

**New Human:**
1. Add to "Humans" table above
2. Update org-chart.md if they have management authority
3. Update staff.md

**New Agent:**
1. Create `.claude/agents/{agent-id}.md` following template
2. Add to "AI Agents" table above
3. Update org-chart.md with reporting relationship
4. Update `.claude/skills/business-context/staff.md` to keep in sync

**New Skill:**
1. Create `.claude/skills/{skill}/SKILL.md` following PSO pattern
2. Add to "Skills" table above
3. Update `.claude/skills/business-context/staff.md` to keep in sync
