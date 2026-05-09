
- add 'requirement.md' file that includes purpose, objectives, contexts, requirements of the project.
- '/init' : start with '/init' in new/existing project directory. it creates CLAUDE.md. Instead of re-explaining the requirements every sessions, Claude contextualize, initialize everything you need for the project.  
- '/usage': know your remaining context.
- '/context': shows what component using your context
- keep your context small. break your requirement into small tasks and make the context window small. 
- '/compact': run '/compact' when your context window reaches 60% or more. It will compress without loosing important information.
- add skills > skills/code-review/SKILL.md, skills/tech-debt/SKILL.md

- Tips:
- - Make Claude to ask question. like 'Continuously ask questions until you are more than 80% confident that you understood the requirements'.
  - Build self-checking into the todo list. add quality check into execution plan.
  - Use sub-agents for parallel  work: use smaller model like Haiku for subagent tasks. and main use for Opus for main complex task. It saves token usages.
   - Use subagents to do 2 parallel tasks.
      - reassess the recommendations and update the suggestions if required.
      - cross validate the recommendations as a peer reviewer.
  - constantly update CLAUDE.md as and when any new feature is added.

  - Research using plan mode. 'Shift+M' to change to plan mode.
  - 
