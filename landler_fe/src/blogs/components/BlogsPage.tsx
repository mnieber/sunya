import { observer } from 'mobx-react-lite';
import React from 'react';
import { withContextProps } from 'react-props-from-context';
import { Route } from 'wouter';
import { BlogPostListView } from '/src/blogPosts/components';
import { BlogPostFormView } from '/src/blogPosts/components/BlogPostFormView';
import { DeleteBlogPostsButton } from '/src/blogPosts/components/DeleteBlogPostsButton';
import { EditBlogPostButton } from '/src/blogPosts/components/EditBlogPostButton';
import { blogPostsCtx } from '/src/blogPosts/hooks/useBlogPostsContext';
import { BlogListView, SelectBlogEffect } from '/src/blogs/components';
import { blogsRoutes } from '/src/blogs/routes';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './BlogsPage.scss';

export const ContextProps = {
  //
  blogPostsEdit: blogPostsCtx.blogPostsEdit,
};

export type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

export const BlogsPage = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <div className={cn('BlogsPage', L.row.bar(), props.className)}>
        {
          // 🔳 LeftSideBar
        }
        <div className={cn('BlogsPage__LeftSideBar')}>
          <BlogListView className={cn()} />
        </div>
        {
          // 🔳 RightCanvas
        }
        <div className={cn('BlogsPage__RightCanvas', L.col.canvas())}>
          <Route path={blogsRoutes.blog()}>
            <SelectBlogEffect />
            <div className={cn(L.col.skewer(), 'p-4')}>
              <BlogPostListView className="mb-4" />
              {props.blogPostsEdit.isEditing && (
                <BlogPostFormView className="mt-4" />
              )}
              <EditBlogPostButton className="mt-8" />
              <DeleteBlogPostsButton className="" />
            </div>
          </Route>
        </div>
      </div>
    );
  }, ContextProps)
);

export const BlogsPageS = {};
