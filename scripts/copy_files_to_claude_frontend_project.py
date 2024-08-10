import shutil
import os
import argparse

landler_fe = "/home/maarten/projects/sunya/src/landler_fe"
fe_code_instructions = (
    "/home/maarten/projects/sunya/src/mock/blogs/frontend/spec/prompts"
)
fe_spec = "/home/maarten/projects/sunya/src/mock/blogs/spec"

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
]

file_map = {
    f"{fe_code_instructions}": "instructions",
    f"{fe_spec}": "spec",
    f"{landler_fe}/src/api/mutations/useCreateBlogPost.ts": "api/mutations",
    f"{landler_fe}/src/api/queries/useGetBlogPosts.ts": "api/queries",
    f"{landler_fe}/src/api/types/BlogPostT.ts": "api/types",
    f"{landler_fe}/src/api/types/BlogT.ts": "api/types",
    f"{landler_fe}/src/app/components/App.scss": "app/components",
    f"{landler_fe}/src/app/components/App.tsx": "app/components",
    f"{landler_fe}/src/blogPosts/BlogPostsState": "blogPosts/BlogPostsState",
    f"{landler_fe}/src/blogPosts/components/BlogPostFormView": "blogPosts/components/BlogPostFormView",
    f"{landler_fe}/src/blogPosts/components/BlogPostListView.scss": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/components/BlogPostListView.tsx": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/components/BlogPostListViewItem.scss": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/components/BlogPostListViewItem.tsx": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/components/BlogPostsStateProvider.tsx": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/components/DeleteBlogPostsButton.tsx": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/components/EditBlogPostButton.tsx": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/components/MarkBlogPostAsPublishedButton.tsx": "blogPosts/components",
    f"{landler_fe}/src/blogPosts/hooks/useBlogPostsContext.ts": "blogPosts/hooks",
    f"{landler_fe}/src/blogPosts/hooks/useBlogPostsState.ts": "blogPosts/hooks",
    f"{landler_fe}/src/blogPosts/routes.ts": "blogPosts",
    f"{landler_fe}/src/blogs/BlogsState": "blogs/BlogsState",
    f"{landler_fe}/src/blogs/components/BlogListView.scss": "blogs/components",
    f"{landler_fe}/src/blogs/components/BlogListView.tsx": "blogs/components",
    f"{landler_fe}/src/blogs/components/BlogListViewItem.scss": "blogs/components",
    f"{landler_fe}/src/blogs/components/BlogListViewItem.tsx": "blogs/components",
    f"{landler_fe}/src/blogs/components/BlogsPage.tsx": "blogs/components",
    f"{landler_fe}/src/blogs/components/BlogsStateProvider.tsx": "blogs/components",
    f"{landler_fe}/src/blogs/components/BlogsSwitch.tsx": "blogs/components",
    f"{landler_fe}/src/blogs/components/SelectBlogEffect.tsx": "blogs/components",
    f"{landler_fe}/src/blogs/hooks/useBlogsContext.ts": "blogs/hooks",
    f"{landler_fe}/src/blogs/hooks/useBlogsState.ts": "blogs/hooks",
    f"{landler_fe}/src/blogs/routes.ts": "blogs",
    f"{landler_fe}/src/forms/components/FormCancelButton.tsx": "forms/components",
    f"{landler_fe}/src/forms/components/FormField.AuthCard.scss": "forms/components",
    f"{landler_fe}/src/forms/components/FormField.MainView.scss": "forms/components",
    f"{landler_fe}/src/forms/components/FormField.tsx": "forms/components",
    f"{landler_fe}/src/forms/components/FormSaveButton.tsx": "forms/components",
    f"{landler_fe}/src/forms/components/NameField.tsx": "forms/components",
    f"{landler_fe}/src/forms/components/TextField.scss": "forms/components",
    f"{landler_fe}/src/forms/components/TextField.tsx": "forms/components",
    f"{landler_fe}/src/frames/components/AccountsMenu.tsx": "frames/components",
    f"{landler_fe}/src/frames/components/DialogButton": "frames/components/DialogButton",
    f"{landler_fe}/src/frames/components/MainView.tsx": "frames/components",
    f"{landler_fe}/src/frames/components/ToolButton": "frames/components/ToolButton",
    f"{landler_fe}/src/frames/layout.ts": "frames",
    f"{landler_fe}/src/mocks/queries/handleGetBlogs.ts": "mocks/queries",
    f"{landler_fe}/src/routes/createNavHandler.ts": "routes",
    f"{landler_fe}/src/routes/navHandler.ts": "routes",
    f"{landler_fe}/src/stories/BlogListView.stories.tsx": "stories",
}


def get_file_inventory(directory):
    inventory = set()
    for root, _, files in os.walk(directory):
        for file in files:
            inventory.add(os.path.join(root, file))
    return inventory


def get_expanded_dir_list():
    result = []
    for dir_entry in dir_list:
        base_dir = dir_entry
        while base_dir:
            if base_dir not in result:
                result.append(base_dir)
            base_dir = os.path.dirname(base_dir)
    return result


def get_files_to_copy(file_map, target_dir, expanded_dir_list):
    files_to_copy = []
    for source, dest in file_map.items():
        if os.path.isfile(source):
            if dest in expanded_dir_list:
                target = os.path.join(target_dir, dest, os.path.basename(source))
            else:
                if "." not in os.path.basename(dest):
                    print(
                        "Warning: No file extension found in destination file: ",
                        dest,
                        "Did you forget to add an entry in the dir_list?",
                    )
                target = os.path.join(target_dir, dest)
            files_to_copy.append((source, target))
        elif os.path.isdir(source):
            for root, _, files in os.walk(source):
                for file in files:
                    src_file = os.path.join(root, file)
                    rel_path = os.path.relpath(src_file, source)
                    target = os.path.join(target_dir, dest, rel_path)
                    files_to_copy.append((src_file, target))
    return files_to_copy


def sync_files(target_dir):
    os.makedirs(target_dir, exist_ok=True)
    file_inventory = get_file_inventory(target_dir)
    files_to_copy = get_files_to_copy(file_map, target_dir, get_expanded_dir_list())

    # Copy files
    for source, target in files_to_copy:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(source, target)
        if target in file_inventory:
            file_inventory.remove(target)

    # Remove files that are no longer needed
    for file in file_inventory:
        if os.path.isfile(file):
            os.remove(file)

    # Remove empty directories
    for root, dirs, files in os.walk(target_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

    return files_to_copy


def parse_args():
    parser = argparse.ArgumentParser(
        description="Synchronize files to a target directory."
    )
    parser.add_argument("target_dir", help="The target directory for synchronization")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase output verbosity"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    files_copied = sync_files(args.target_dir)

    if args.verbose:
        print(f"Synced {len(files_copied)} files.")
