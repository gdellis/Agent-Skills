---
name: "artifacts"
description: "Create or publish downloadable files, and read or edit previously published artifacts."
---
# Downloadable artifacts

Use this workflow to deliver verified files through automatic download cards.

1. Unless the execution environment is already upgraded, call `upgrade_execution_environment` before reading, editing, or publishing files in `/home/user/artifacts`. The artifact directory is mounted only after the upgrade succeeds.
2. Prepare and verify the requested deliverables. Keep scripts, intermediate results, and scratch files in the working directory outside `/home/user/artifacts`.
3. Write or copy the completed files into `/home/user/artifacts`. For a small text file, write it directly there with `write_file` after the upgrade. Bash commands and filesystem writes to this directory publish files and return a `files` list containing their names and download URLs. Keep commands in the foreground so publication waits for them to finish.
4. Inspect the tool result and confirm that publication returned the file. The product automatically displays its download card, so do not repeat the returned URL as a Markdown link. A local path is not a download link. Claim a file is ready only when publication succeeded and its content has been verified.

A single edit can be made directly to an artifact. For several edits across tool calls, copy the file outside `/home/user/artifacts`, edit and verify that working copy, then copy the finished file back once. Each tool call that changes an artifact publishes a new version.

A failed command can still publish files; inspect both the execution result and returned files before reporting success. If publication fails, preserve completed work, report the failure, and avoid rerunning computation or external effects merely to obtain a link.

For an existing Canvas, use its export/download control when it supports the requested format. Do not republish the same deliverable through this workflow when Canvas already provides the requested download. If the user requests a different format that Canvas cannot export, create and publish that separate file through this workflow.