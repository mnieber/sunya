/*
In this file we see how the "BlogPostsState" is provided by the BlogPostsStateProvider.
The BlogPostsFilter, BlogPostListView and DeleteBlogPostsButton will consume the provided state
by using the default properties that BlogPostsStateProvider provides.

Continue by:
- reading the BlogPostsStateProvider.tsx file.
- reading the BlogPostsFilter.tsx, BlogPostListView.tsx and DeleteBlogPostsButton.tsx files.
*/

import { QueryClientProvider } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';
import { BlogPostListView } from '/src/blogPosts/components';
import { BlogPostsFilter } from '/src/blogPosts/components/BlogPostsFilter';
import { BlogPostsStateProvider } from '/src/blogPosts/components/BlogPostsStateProvider';
import { DeleteBlogPostsButton } from '/src/blogPosts/components/DeleteBlogPostsButton';
import { cn } from '/src/utils/classnames';

// Import styles
import './App.scss';

export const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <BlogPostsStateProvider>
        <div className={cn('App')}>
          <div className={cn('App__Body', 'flex flex-col items-center')}>
            <BlogPostsFilter />
            <BlogPostListView />
            <DeleteBlogPostsButton className="mt-8" />
          </div>
        </div>
      </BlogPostsStateProvider>
    </QueryClientProvider>
  );
};
