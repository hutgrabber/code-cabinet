return {
  "williamboman/mason.nvim",
  opts = {
    auto_install = true,
    ensure_installed = {
      "pyright",
      "mypy",
      "ruff",
    },
  },
}
