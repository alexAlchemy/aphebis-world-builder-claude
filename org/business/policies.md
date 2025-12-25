# Business Policies

## Financial Policy

### Budget Principles

- **Zero funding = zero waste** - Every dollar must earn its keep
- **Subscription scrutiny** - No recurring costs without proven ROI
- **Bootstrapped mindset** - Free/self-hosted solutions preferred over SaaS
- **Smart spending** - If we pay, it must directly accelerate revenue or product quality

### Decision Framework for Expenses

| Expense Type | Decision Criteria |
|--------------|-------------------|
| **Tool subscriptions** | Must prove ROI within 30 days or cancel |
| **Infrastructure** | Cheapest viable option first, scale when needed |
| **Marketing/Ads** | Small tests first, scale only with positive unit economics |
| **Contractors** | Project-based only, no ongoing commitments until funding |

### Approval Authority

| Amount | Approval |
|--------|----------|
| <$50 | Alex can approve immediately |
| $50-$200 | Requires 24-hour consideration period |
| $200-$1000 | Must pass ROI test documented in writing |
| >$1000 | Not possible without funding |

## Risk Policy

### Our Risk Tolerance

As a bootstrapped startup, we can take risks that funded companies cannot:

- **Technical risk** - We can try novel approaches, fail fast, iterate
- **Market risk** - We can target underserved niches, experiment with positioning
- **Product risk** - We can ship MVPs, test with real users, pivot quickly

### Risks We Avoid

- **Legal/compliance risk** - No gray areas with data privacy, IP, regulations
- **Security risk** - No shortcuts on auth, encryption, data protection
- **Vendor lock-in** - Prefer open standards, portable data, avoid proprietary ecosystems

## Technical Policies

### Architecture Principles

1. **Agent-first** - Build for AI agent workforce, not just human developers
2. **MCP-native** - Leverage Model Context Protocol for integrations
3. **Simple scales** - Start simple, add complexity only when needed
4. **Document everything** - Future agents will need context too

### Technology Choices

| Category | Preference | Rationale |
|----------|------------|-----------|
| **LLM provider** | Anthropic Claude | Quality, tool use, context window |
| **Agent framework** | Claude Code CLI | Native environment, good tool support |
| **Data storage** | Plain text/JSON files | No infrastructure, version controlled, debuggable |
| **Deployment** | TBD | Will address when we have users |

## Communication Policy

### Internal Communication

- **Default to text** - Everything written = searchable, referenceable
- **Document decisions** - Record in org/engineering/ or org/projects/
- **Assume async** - Agents are async-first; humans should be too

### External Communication

- **Honest about stage** - We're early, we're learning, we iterate
- **Under-promise, over-deliver** - Better to surprise than disappoint
- **No vaporware** - Don't announce what we haven't built

## Development Policy

### Ship Velocity

- **Done > Perfect** - Ship it, get feedback, improve
- **Week-not-months** - If it takes more than a week, break it down
- **User contact** - Talk to users every week, even (especially) when product is rough

### Code Quality

- **Clean enough** - Code should be readable, but we're not building cathedrals
- **Delete > Refactor** - Unused code? Delete it. No "might need later"
- **Test what matters** - Core paths need tests; edge cases can wait

## Hiring (Human) Policy

### Current Status: Not Hiring

We're pre-revenue, pre-funding. Adding humans would burn runway we don't have.

### When We Do Hire (Eventually)

- **Hustlers first** - People who ship, not just plan
- **Generalists preferred** - Small team = everyone wears multiple hats
- **AI-native mindset** - Must be comfortable working alongside AI agents
- **Equity-heavy** - We can't pay market rates; compensation will be mostly ownership

## Hiring (Agent) Policy

### We Hire Agents Freely

Creating new agents is cheap and scales infinitely. We're building an AI workforce.

### Agent Creation Criteria

Create a new agent when:
1. Distinct expertise domain (not just "another coder")
2. Repeated need for this expertise across projects
3. Can be defined with clear scope and boundaries
4. Would provide ROI through better decisions/faster work

## Project Policy

All project work flows through the PSO (Project Support Officer):
- Create project before starting work
- Record activities as you go
- Save artifacts to project folders
- Close projects when done

See `.claude/skills/pso/SKILL.md` for PSO protocols.

## Open Questions

Policy is living. These are unresolved:

| Question | Status | Owner |
|----------|--------|-------|
| IP protection strategy before launch | TBD | Alex |
| Customer support approach (no humans yet) | TBD | Business Manager |
| Revenue model specifics | TBD | Alex + Business Manager |
| Hosting/deployment strategy | TBD | Technical Strategy Advisor |
