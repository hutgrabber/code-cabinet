return {
  { -- Set default Colorscheme
    "LazyVim/LazyVim",
    opts = {
      colorscheme = { "dracula" },
    },
  },
  { -- Nord Colorscheme
    "gbprod/nord.nvim",
    lazy = false,
    priority = 1000,
  },
  { -- Tokyo Night Colorscheme
    "folke/tokyonight.nvim",
    lazy = false,
    priority = 1000,
  },
  { -- Rose Pine Colorscheme
    "rose-pine/neovim",
    lazy = false,
    priority = 1000,
  },
  { -- Dracula Colorscheme
    "mofiqul/dracula.nvim",
    lazy = false,
    priority = 1000,
  },
  -- { Template
  --   "Github/repo",
  --   lazy = false,
  --   priority = 1000,
  -- }
}
