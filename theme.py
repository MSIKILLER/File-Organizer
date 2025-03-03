def toggle_theme(dark_mode, root, label, folder_entry, browse_button, convert_button, exit_button, toggle_button, summary_text):
    if dark_mode:
        new_bg = "white"
        new_fg = "black"
        toggle_button.config(text="Dark Theme OFF")
    else:
        new_bg = "#2E2E2E"
        new_fg = "white"
        toggle_button.config(text="Dark Theme ON")

    root.config(bg=new_bg)
    label.config(bg=new_bg, fg=new_fg)
    folder_entry.config(bg=new_bg, fg=new_fg)
    browse_button.config(bg=new_bg, fg=new_fg)
    convert_button.config(bg=new_bg, fg=new_fg)
    exit_button.config(bg=new_bg, fg=new_fg)
    toggle_button.config(bg=new_bg, fg=new_fg)
    summary_text.config(bg=new_bg, fg=new_fg)

    return not dark_mode