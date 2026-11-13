# Generated from scripts/python-activation/activate.sh.template by `pnpm generate:python-activation`; do not edit.
# Source in the same bash command as each Python run, after upgrading the
# sandbox. The bash tool runs commands with POSIX sh, so keep this file POSIX: a
# sourced script cannot locate itself there, hence the fixed skill mount path.
_le_chat_python_library=/home/user/skills/data-analysis/python/library
_le_chat_import_paths=""

_le_chat_activate_python() {
    # Lightweight bash has no Python and cannot run the commands below.
    if ! command -v python >/dev/null 2>&1; then
        echo 'Python is not available in lightweight bash; call `upgrade_execution_environment` first, then run this command again.' >&2
        return 1
    fi

    _le_chat_digest=$(sha256sum -- "$_le_chat_python_library/bundles/requirements.txt") || return
    _le_chat_cache="/tmp/le-chat-native-python/${_le_chat_digest%% *}"

    # Publish a complete extraction so concurrent Python processes never see a
    # partially written native extension. The mounted archive stays read-only.
    if [ ! -d "$_le_chat_cache" ]; then
        mkdir -p /tmp/le-chat-native-python || return
        _le_chat_staging=$(mktemp -d "${_le_chat_cache}.XXXXXX") || return
        if ! unzip -q "$_le_chat_python_library/.bundled/python.zip" -d "$_le_chat_staging"; then
            rm -rf -- "$_le_chat_staging"
            return 1
        fi
        if ! mv -- "$_le_chat_staging" "$_le_chat_cache" 2>/dev/null; then
            rm -rf -- "$_le_chat_staging"
            [ -d "$_le_chat_cache" ] || return 1
        fi
        # If another process published first, mv moved this copy inside it.
        rm -rf -- "$_le_chat_cache/${_le_chat_staging##*/}"
    fi

    # Scripts run with the safe path, and startup/sitecustomize.py appends the
    # script's folder last, so a script named like a module cannot shadow it.
    export PYTHONPATH="$_le_chat_python_library/startup:$_le_chat_import_paths$_le_chat_cache${PYTHONPATH:+:$PYTHONPATH}"
    export PYTHONSAFEPATH=1
    # Plots render to files; the sandbox has no display.
    export MPLBACKEND=Agg
}

# Capture the status in a condition so callers using `set -e` still clean up.
_le_chat_status=0
_le_chat_activate_python || _le_chat_status=$?
unset -f _le_chat_activate_python
unset _le_chat_python_library _le_chat_import_paths _le_chat_digest _le_chat_cache _le_chat_staging
[ "$_le_chat_status" -eq 0 ] || { unset _le_chat_status; return 1; }
unset _le_chat_status
