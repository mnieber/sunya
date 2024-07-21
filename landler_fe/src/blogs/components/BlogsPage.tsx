import React from 'react';
import { Route } from 'wouter';
import { BlogPostListView } from '/src/blogPosts/components';
import { DeleteBlogPostsButton } from '/src/blogPosts/components/DeleteBlogPostsButton';
import { BlogListView, SelectBlogEffect } from '/src/blogs/components';
import { type BlogsRoutesT } from '/src/blogs/routeTable';
import { L } from '/src/frames/layout';
import { getRouteFns } from '/src/routes/routeTable';
import { cn } from '/src/utils/classnames';

// Import styles
import './BlogsPage.scss';

type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

export const BlogsPage = (props: PropsT) => {
  const routeFns = getRouteFns<BlogsRoutesT>();

  return (
    <div className={cn('BlogsPage', L.row.bar(), props.className)}>
      <BlogListView className={cn()} />
      <Route path={routeFns.blog()}>
        <SelectBlogEffect />
        <div className={cn(L.col.skewer(), 'p-4')}>
          <BlogPostListView />
          <DeleteBlogPostsButton className="mt-8" />
        </div>
      </Route>
    </div>
  );
};

export const BlogsPageS = {};
