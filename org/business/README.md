# Business Context

This directory contains the shared business context for Aphebis. All agents and skills can reference this information to understand the organization they work for.

## Purpose

Without a central business context, every agent would need business information baked into its definition. This doesn't scale:
- Updates require editing every agent file
- Information drifts between agents
- No single source of truth

**Solution:** This directory is the single source of truth. The `business-context` skill provides read-only access to all agents.

## Files

| File | Contents | Updated |
|------|----------|---------|
| `company.md` | Company identity, stage, industry, description | 2025-12-25 |
| `mission.md` | Mission, vision, values, what we're not | 2025-12-25 |
| `org-chart.md` | Organizational structure, reporting relationships | 2025-12-25 |
| `staff.md` | Humans, AI agents, skills, contact protocols | 2025-12-25 |
| `policies.md` | Financial, risk, technical, communication policies | 2025-12-25 |
| `README.md` | This file | 2025-12-25 |

## How to Use

### For Agents

When you need business context, invoke the `business-context` skill:

```
"Before I advise on this decision, I need to understand our company's risk tolerance."
→ Invoke business-context skill, query: "policies"
→ Returns policies.md content
```

### For Humans

**To update business context:**
1. Edit the relevant file directly in `org/business/`
2. Commit to git for version control
3. All agents immediately have access to updated context

**To add new context categories:**
1. Create new `.md` file in `org/business/`
2. Add reference in this README
3. Update `business-context` skill to recognize the new category

## Maintenance

- **Keep it current** - Stale context is worse than no context
- **Keep it concise** - Agents work best with focused information
- **Keep it structured** - Use consistent formatting for machine readability
- **Document changes** - Git commit messages should describe what changed and why

## Related Documentation

- `.claude/skills/business-context/SKILL.md` - Skill definition for accessing this data
- `org/engineering/agent-skill-architecture.md` - Overall org architecture
- `.claude/agents/*.md` - Individual agent definitions
