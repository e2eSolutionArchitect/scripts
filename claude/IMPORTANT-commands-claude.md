
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
