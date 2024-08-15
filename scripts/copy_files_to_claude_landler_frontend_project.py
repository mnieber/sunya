import sync_files_to_local_claude_dir

in_landler_fe = "/home/maarten/projects/sunya/src/landler_fe"
in_fe_code_instructions = (
    "/home/maarten/projects/sunya/src/mock/blogs/frontend/spec/prompts"
)
in_fe_spec = "/home/maarten/projects/sunya/src/mock/blogs/spec"

dir_list = [
    "api/mutations",
    "api/queries",
    "api/types",
    "app/components",
    "blogPosts",
    "blogPosts/BlogPostsState",
    "blogPosts/components",
    "blogPosts/components/BlogPostFormView",
    "blogPosts/components/BlogPostFormView",
    "blogPosts/hooks",
    "blogs",
    "blogs/components",
    "blogs/hooks",
    "forms/components",
    "frames",
    "frames/components",
    "frames/components/DialogButton",
    "frames/components/ToolButton",
    "instructions",
    "mocks/queries",
    "routes",
    "stories",
    "spec",
]

file_map = {
    f"{in_fe_code_instructions}/instructions*.md": "instructions",
    f"{in_fe_spec}/roadmap.md": "spec",
    f"{in_fe_spec}/modules": "spec/modules",
    f"{in_fe_spec}/scenarios": "spec/scenarios",
    f"{in_landler_fe}/src/api/mutations/useCreateBlogPost.ts": "api/mutations",
    f"{in_landler_fe}/src/api/queries/useGetBlogPosts.ts": "api/queries",
    f"{in_landler_fe}/src/api/types/*T.ts": "api/types",
    f"{in_landler_fe}/src/app/components/App.*": "app/components",
    f"{in_landler_fe}/src/blogPosts/BlogPostsState": "blogPosts/BlogPostsState",
    f"{in_landler_fe}/src/blogPosts/components/BlogPostFormView": "blogPosts/components/BlogPostFormView",
    f"{in_landler_fe}/src/blogPosts/components/BlogPostListView.*": "blogPosts/components",
    f"{in_landler_fe}/src/blogPosts/components/BlogPostListViewItem.*": "blogPosts/components",
    f"{in_landler_fe}/src/blogPosts/components/BlogPostsStateProvider.tsx": "blogPosts/components",
    f"{in_landler_fe}/src/blogPosts/components/DeleteBlogPostsButton.tsx": "blogPosts/components",
    f"{in_landler_fe}/src/blogPosts/components/EditBlogPostButton.tsx": "blogPosts/components",
    f"{in_landler_fe}/src/blogPosts/components/MarkBlogPostAsPublishedButton.tsx": "blogPosts/components",
    f"{in_landler_fe}/src/blogPosts/hooks/useBlogPostsContext.ts": "blogPosts/hooks",
    f"{in_landler_fe}/src/blogPosts/hooks/useBlogPostsState.ts": "blogPosts/hooks",
    f"{in_landler_fe}/src/blogPosts/routes.ts": "blogPosts",
    f"{in_landler_fe}/src/blogs/BlogsState": "blogs/BlogsState",
    f"{in_landler_fe}/src/blogs/components/BlogListView.*": "blogs/components",
    f"{in_landler_fe}/src/blogs/components/BlogListViewItem.*": "blogs/components",
    f"{in_landler_fe}/src/blogs/components/BlogsPage.tsx": "blogs/components",
    f"{in_landler_fe}/src/blogs/components/BlogsStateProvider.tsx": "blogs/components",
    f"{in_landler_fe}/src/blogs/components/BlogsSwitch.tsx": "blogs/components",
    f"{in_landler_fe}/src/blogs/components/SelectBlogEffect.tsx": "blogs/components",
    f"{in_landler_fe}/src/blogs/hooks/useBlogsContext.ts": "blogs/hooks",
    f"{in_landler_fe}/src/blogs/hooks/useBlogsState.ts": "blogs/hooks",
    f"{in_landler_fe}/src/blogs/routes.ts": "blogs",
    f"{in_landler_fe}/src/forms/components/FormCancelButton.tsx": "forms/components",
    f"{in_landler_fe}/src/forms/components/FormField.AuthCard.scss": "forms/components",
    f"{in_landler_fe}/src/forms/components/FormField.MainView.scss": "forms/components",
    f"{in_landler_fe}/src/forms/components/FormField.tsx": "forms/components",
    f"{in_landler_fe}/src/forms/components/FormSaveButton.tsx": "forms/components",
    f"{in_landler_fe}/src/forms/components/NameField.tsx": "forms/components",
    f"{in_landler_fe}/src/forms/components/TextField.*": "forms/components",
    f"{in_landler_fe}/src/frames/components/AccountsMenu.tsx": "frames/components",
    f"{in_landler_fe}/src/frames/components/DialogButton": "frames/components/DialogButton",
    f"{in_landler_fe}/src/frames/components/MainView.tsx": "frames/components",
    f"{in_landler_fe}/src/frames/components/ToolButton": "frames/components/ToolButton",
    f"{in_landler_fe}/src/frames/layout.ts": "frames",
    f"{in_landler_fe}/src/mocks/queries/handleGetBlogs.ts": "mocks/queries",
    f"{in_landler_fe}/src/routes/createNavHandler.ts": "routes",
    f"{in_landler_fe}/src/routes/navHandler.ts": "routes",
    f"{in_landler_fe}/src/stories/BlogListView.stories.tsx": "stories",
}


if __name__ == "__main__":
    args = sync_files_to_local_claude_dir.parse_args()
    files_copied = sync_files_to_local_claude_dir.sync_files(
        file_map, dir_list, args.target_dir
    )

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
