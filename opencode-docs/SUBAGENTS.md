Subagents
Subagents are specialized assistants that primary agents can invoke for specific tasks. You can also manually invoke them by @ mentioning them in your messages.

Built-in
OpenCode comes with two built-in primary agents and two built-in subagents.

Build
Mode: primary

Build is the default primary agent with all tools enabled. This is the standard agent for development work where you need full access to file operations and system commands.

Plan
Mode: primary

A restricted agent designed for planning and analysis. We use a permission system to give you more control and prevent unintended changes. By default, all of the following are set to ask:

file edits: All writes, patches, and edits
bash: All bash commands
This agent is useful when you want the LLM to analyze code, suggest changes, or create plans without making any actual modifications to your codebase.

General
Mode: subagent

A general-purpose agent for researching complex questions and executing multi-step tasks. Has full tool access (except todo), so it can make file changes when needed. Use this to run multiple units of work in parallel.

Explore
Mode: subagent

A fast, read-only agent for exploring codebases. Cannot modify files. Use this when you need to quickly find files by patterns, search code for keywords, or answer questions about the codebase.


Subagents can be invoked:

Automatically by primary agents for specialized tasks based on their descriptions.

Manually by @ mentioning a subagent in your message. For example:
@general help me search for this function

Configure
You can customize the built-in agents or create your own through configuration.

Markdown
You can define agents using markdown files. Place them in:

Per-project: .opencode/agents/