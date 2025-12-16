# Magnus the World Builder

An intelligent world-building companion skill for the Aphebis platform that helps you explore, discuss, and create rich fictional worlds through collaborative AI assistance.

## Overview

Magnus is a specialized AI skill designed to work with Aphebis—an AI-driven character simulation platform that creates autonomous NPCs through cognitive modeling. As an ancient lorekeeper and master world-builder, Magnus helps you craft immersive fictional worlds with deep narrative potential, environmental storytelling, and meaningful interconnections.

## Features

### 🗺️ Discovery-First Approach
- Browse existing worlds, areas, and locations
- Understand world structure and lore before creating
- Query-based exploration to avoid duplication

### 💡 Collaborative Brainstorming
- Multiple creative options for every decision (3-5 alternatives)
- Evocative, descriptive language that inspires imagination
- "What if" scenario exploration and narrative analysis

### 🏗️ Structured World-Building
- **Hierarchical Organization**: World → Area → Location
- **Incremental Building**: Layer worlds progressively from concept to detail
- **Confirmation-Required**: Never creates without explicit user approval

### 🎭 Narrative-Focused Design
- Emphasizes dramatic potential and NPC agency
- Environmental storytelling elements
- Interconnected locations with narrative hooks

## World Structure

Aphebis organizes fictional worlds in three tiers:

```
World (e.g., "The Shattered Kingdoms", "Neo-Tokyo 2087")
  ├── Area (e.g., "The Thornwood Forest", "District 7")
  │     ├── Location (e.g., "The Witch's Hollow")
  │     ├── Location (e.g., "Ancient Oak Crossing")
  │     └── ...
  ├── Area
  └── ...
```

## Creative Philosophy

Magnus guides world-building through four key considerations:

- **Dramatic Potential** - What conflicts, alliances, or tensions could emerge?
- **NPC Agency** - What goals might autonomous characters pursue here?
- **Environmental Storytelling** - What stories do locations tell through their details?
- **Interconnection** - How do places relate to others in the world?

## Example Workflows

### Exploring an Existing World
```
User: "Tell me about the Iron Dominion"
Magnus:
  1. Searches for world by name
  2. Retrieves all areas in that world
  3. Describes the structure and offers to explore specific areas
  4. Asks: "Which area interests you? Or shall we add a new region?"
```

### Creating from Scratch
```
User: "I want a cyberpunk world"
Magnus:
  1. Brainstorms 3-5 world names with brief concepts
  2. After user chooses, suggests rich description
  3. Confirms world details before creating
  4. Immediately brainstorms 2-3 initial areas
  5. Creates areas only after user approval
```

### Expanding an Area
```
User: "Add locations to the Thornwood"
Magnus:
  1. Retrieves the area to confirm it exists
  2. Lists existing locations in that area
  3. Asks about the kind of locations envisioned
  4. Proposes 3-5 specific location ideas
  5. Creates locations one at a time with confirmation
```

## Getting Started

### Prerequisites
- Access to the Aphebis platform
- Claude Desktop or compatible AI assistant supporting MCP skills

### Installation
1. Clone this repository
2. Add the skill to your MCP configuration
3. Start building worlds with Magnus!

## Project Structure

```
magnus-the-world-builder/
├── magnus-the-world-builder.skill  # Skill definition file
├── SKILL.md                        # Detailed skill documentation
├── assets/                         # Skill assets and resources
├── references/
│   ├── iron-domination-example.md  # Example world structure
│   └── prompts.md                  # Brainstorming prompts and patterns
└── scripts/
    └── package.py                  # Packaging utilities
```

## Key Principles

### Safety First
- **Always confirm** before creating, updating, or deleting
- **Query before creating** to avoid duplicates
- **Never invent data** that doesn't exist in the database

### Collaborative Design
- User drives the creative vision
- Magnus offers guidance and multiple options
- Clarifying questions to understand intent
- Evocative language that inspires imagination

### Incremental Building
- Start with compelling world concept
- Add 2-3 major areas that define geography/culture
- Populate areas with specific locations as needed
- Iterate based on creative inspiration

## Example Worlds

Check out [iron-domination-example.md](magnus-the-world-builder/references/iron-domination-example.md) for a complete example of a world structure, featuring:
- Fractured mech empire in radioactive wasteland
- 4 major regions (27 total areas)
- Rich thematic elements and narrative hooks
- Environmental storytelling and dramatic potential

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is part of the Aphebis platform ecosystem.

## About Aphebis

Aphebis is an AI-driven character simulation platform that creates autonomous NPCs through cognitive modeling:
- **Perception** → **Attention** → **Memory** → **Appraisal** → **Decision** → **Reflection**

This cognitive architecture enables NPCs to act as independent agents with goals, memories, and emergent behaviors within the fictional worlds you create.

---

**Start building worlds.** Ask Magnus anything about exploring, discussing, or creating fictional universes for your Aphebis simulations.
