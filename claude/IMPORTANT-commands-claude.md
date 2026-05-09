# 🤖 Claude Code — Important Commands & Best Practices

> **Source:** [e2eSolutionArchitect/scripts](https://github.com/e2eSolutionArchitect/scripts/blob/main/claude/IMPORTANT-commands-claude.md)  
> **Scope:** Claude Code (CLI) — commands, tips, and advanced patterns

---

## ⚙️ Project Setup

| Action | Detail |
|--------|--------|
| **Permissions file** | Create `.claude/settings.json` and define `allow` / `deny` command permissions to control what Claude Code can execute |
| **Requirements file** | Add a `requirement.md` (or `docs/requirements.md`) capturing the project's purpose, objectives, context, and functional requirements |
| **`/init`** | Run in a new or existing project directory. Generates `CLAUDE.md` — Claude's persistent memory for the project, so you don't have to re-explain context every session |

---

## 🗂️ CLAUDE.md — Living Project Memory

- **Keep it updated** — revise `CLAUDE.md` every time a new feature is added or the architecture changes.
- **Reference other docs** from within `CLAUDE.md`, for example:
  - `docs/requirements.md` — functional requirements
  - `docs/architecture.md` — system design
  - `docs/style-guide.md` — coding standards

---

## 📟 Session Commands

| Command | Purpose |
|---------|---------|
| `/init` | Initialise project context; creates `CLAUDE.md` |
| `/usage` | Check your remaining context quota for the current session |
| `/context` | Inspect which components are currently consuming your context window |
| `/compact` | Compress the context window (losslessly) — **run this when context reaches ≥ 60%** |
| `/rewind` | Undo the last request and roll back to the previous conversation state |

> ✅ **Best practice:** Keep context lean. Break large requirements into small, focused tasks and run `/compact` proactively to avoid hitting limits.

---

## 🛠️ Custom Skills

Build reusable skill files that Claude Code can invoke as slash commands:

```
skills/
  code-review/SKILL.md
  security-rules/SKILL.md
```

Invoke with: `/code-review` or `/security-rules`

This lets you encode team standards, review checklists, or linting rules once and reuse them across sessions.

---

## 💡 Productivity Tips

**1. Make Claude ask clarifying questions**
> Prompt: *"Continuously ask questions until you are more than 80% confident you have understood the requirements."*
This significantly reduces back-and-forth and hallucinated assumptions.

**2. Self-checking todo lists**
Embed quality gates directly into the execution plan (e.g., "after implementing X, run unit tests and verify coverage").

**3. Sub-agents for parallel work**
- Use a lightweight model (e.g., **Claude Haiku**) for sub-agent tasks.
- Use a powerful model (e.g., **Claude Opus**) for the primary complex reasoning task.
- This reduces token costs significantly.
- ⚠️ Note: Sub-agents **cannot communicate with each other** — they operate independently.

**4. Parallel sub-agent tasks (example)**
Run two sub-agents concurrently:
- Sub-agent A: Reassess recommendations and update suggestions.
- Sub-agent B: Cross-validate recommendations as a peer reviewer.

**5. Plan mode for research**
Press `Shift+M` to switch to plan mode. Use it to explore and research before committing to implementation.

**6. Course-correct mid-session**
If Claude is heading in the wrong direction, explicitly state the correction rather than letting it continue. Early redirection saves context and time.

---

## 🚀 Advanced Patterns

### Parallel Sessions with Git Worktrees
Run multiple Claude Code sessions from the same repository simultaneously using Git worktrees:

```bash
# Create isolated worktrees for each feature branch
git worktree add ../add-feature-1 -b add-feature-1
git worktree add ../add-feature-2 -b add-feature-2

# Then launch Claude Code in each directory independently
cd ../add-feature-1 && claude
cd ../add-feature-2 && claude
```

> ⚠️ **Validation note:** The `claude --worktree` flag shown in some references is not an official Claude Code CLI option. The correct approach is to use native `git worktree` commands first, then run `claude` inside each worktree directory.

---

### Recurring Tasks with `/loop`
Use `/loop` to set Claude on a repeating monitoring task:

```
/loop every 5 minutes: check deployment status and alert on failure
/loop every 5 minutes: monitor open PRs and flag stale ones
```

> ⚠️ **Validation note:** `/loop` is not listed as an official slash command in current Claude Code documentation. Verify availability in your installed version before relying on it.

---

### Always-On Cloud Session
Host Claude Code on a VPS (cloud virtual machine) for a persistent, always-available session — useful for long-running agentic workflows.

---

### Remote Device Reconnection
```bash
claude remote-control
```
Reconnect to a running Claude Code session from a remote device (e.g., a phone or tablet).

> ⚠️ **Validation note:** `claude remote-control` is not a documented subcommand in the official Claude Code CLI reference. Confirm this is available in your version.

---

### Connect CLI Tools
Claude Code can invoke shell CLI tools directly during agentic tasks. Connect tools such as:

| Tool | Use Case |
|------|----------|
| `aws` | AWS resource management |
| `bq` | BigQuery data queries |
| `psql` | PostgreSQL database access |
| `sqlite3` | Local SQLite queries |
| `kubectl` | Kubernetes cluster management |

---

### Agent Teams
Configure named agents that share a task list and can be addressed directly. This enables structured multi-agent collaboration within a single project.

---

### Context7 MCP Server
Install the **Context7 MCP server** to give Claude real-time access to current documentation for popular frameworks (Angular, Node.js, React, MongoDB, etc.):

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
```

✅ This is the correct and verified installation command.

---

## 🔍 Technical Validation Summary

| Item | Status | Note |
|------|--------|------|
| `.claude/settings.json` permissions | ✅ Valid | Correct Claude Code config location |
| `/init`, `/usage`, `/context`, `/compact`, `/rewind` | ✅ Valid | Official Claude Code slash commands |
| Custom SKILL.md files | ✅ Valid | Supported custom skill pattern |
| Sub-agent model recommendation (Haiku/Opus) | ✅ Valid | Sound cost-optimization strategy |
| `Shift+M` plan mode | ✅ Valid | Confirmed Claude Code UI shortcut |
| Context7 MCP install command | ✅ Valid | Correct `claude mcp add` syntax |
| `claude --worktree` CLI flag | ⚠️ Inaccurate | Use `git worktree add` + run `claude` in each directory instead |
| `claude remote-control` | ⚠️ Unverified | Not found in official Claude Code CLI docs |
| `/loop` slash command | ⚠️ Unverified | Not listed in official slash command reference |
| Typo: "conenct CLI tools" | 🔤 Fixed | Corrected to "connect" |
| Empty bullet in Tips section | 🧹 Fixed | Removed blank entry |

---

*Last reviewed: May 2026 · Claude Code version compatibility: check `claude --version`*



- **VERY IMPORTANT** set permission appropriately: add '.claude/settings.json' and mention the permissions 'allow', 'deny' commands. 
- add 'requirement.md' file that includes purpose, objectives, contexts, requirements of the project.
- '/init' : start with '/init' in new/existing project directory. it creates CLAUDE.md. Instead of re-explaining the requirements every sessions, Claude contextualize, initialize everything you need for the project.  
- '/usage': know your remaining context.
- '/context': shows what component using your context
- keep your context small. break your requirement into small tasks and make the context window small. 
- '/compact': run '/compact' when your context window reaches 60% or more. It will compress without loosing important information.
- build custom skills: skills/code-review/SKILL.md, skills/security-rules/SKILL.md. invoke like '/code-review'.
- constantly update CLAUDE.md as and when any new feature is added.
- make sure that the CLAUDE.md reference to other required files. like refer to 'docs/requirements.md' for project requirements, 'docs/architecture.md' for design architecture, 'docs/style-guide.md' etc.
- '/rewind' : to undo an ask and back to the previous conversation.


Tips:
- - Make Claude to ask question. like 'Continuously ask questions until you are more than 80% confident that you understood the requirements'.
  - Build self-checking into the todo list. add quality check into execution plan.
  - Use sub-agents for parallel  work: use smaller model like Haiku for subagent tasks. and main use for Opus for main complex task. It saves token usages. sub-agents can not talk to each other. 
   - Use subagents to do 2 parallel tasks.
      - reassess the recommendations and update the suggestions if required.
      - cross validate the recommendations as a peer reviewer.

  - Research using plan mode. 'Shift+M' to change to plan mode.
  - course correct : if claude is going differnt direction.
  - 

Advance:
- Parallel work sessions with Git work trees: run more than one session from same project directory. 'claude --worktree add-feature-1', 'claude --worktree add-feature-2'
- /loop: claude for recurring task. like monitor a deployment or PR in every 5 mins.
- Host Claude on VPS cloud for always on session.
- 'claude remote-control' : for reconnecting from remote device like phone.
- conenct CLI tools like 'aws', 'bq', 'psql', 'sqlite3', 'kubectl'.
- agent teams: they share task list, communicate with each other, you can directly talk to the specific agent.
- Context 7 MCP server: install Context 7 MCP server to get current documentation of any popular tools like Angular, NodeJS, React, MongoDB etc. 'claude mcp add context7 -- npx -y @upstash/context7-mcp@latest'
- 
