/*
Just like BlogPostsFilter, the BlogPostListView is quite simple. It shows all the blogPosts, using the
selection and highlight information that comes from blogPostsState.blogPostsCtr.selection and
blogPostsState.blogPostsCtr.highlight (it accesses these facets through the default properties, so that
the component is not tightly coupled to BlogPostsState).

BlogPostListView uses a SelectionUIConnector to handle mouse clicks by (de)selecting blogPosts.
It uses createSelectionKeyHandlers and a KeyboardEventHandler to update the selection using
keyboard events.

BlogPostListView uses isLoading to inspect the resource state of the blogPosts. When you inspect the
code of BlogPostListViewItem, you will see that it uses the isUpdating function to inspect the
resource state of the blogPost that it renders. The item will blink if the blogPost is updating
(this is the case when the blogPost is being deleted).
*/
import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import KeyboardEventHandler from 'react-keyboard-event-handler';
import { withContextProps } from 'react-props-from-context';
import {
  SelectionUIConnector,
  createSelectionKeyHandlers,
} from 'skandha-facets';
import { BlogPostT } from '/src/api/types';
import { BlogPostListViewItem } from '/src/blogPosts/components';
import { blogPostsCtx } from '/src/blogPosts/hooks/useBlogPostsContext';
import { isLoading } from '/src/resourceStates/getState';
import { createKeyDownHandler } from '/src/utils';

// Import styles
import './BlogPostListView.scss';

export type PropsT = {};

const ContextProps = {
  blogPosts: blogPostsCtx.blogPosts,
  blogPostsSelection: blogPostsCtx.blogPostsSelection,
  blogPostsHighlight: blogPostsCtx.blogPostsHighlight,
};

export const BlogPostListView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (isLoading(props.blogPosts)) {
      return <div>Loading...</div>;
    }

    // This UI connecter creates a mouseclick-handler for
    // each BlogPostListViewItem.
    const selectionUIConnector = new SelectionUIConnector({
      selection: props.blogPostsSelection,
    });

    // I prefer to handle key-events in a KeyboardEventHandler instead
    // of handling them in the BlogPostListViewItem.
    const keyHandlers = createSelectionKeyHandlers(props.blogPostsSelection);

    const blogPostDivs = props.blogPosts.map((blogPost: BlogPostT) => (
      <BlogPostListViewItem
        key={blogPost.id}
        className={{
          'BlogPostListViewItem--selected':
            props.blogPostsSelection.itemIds.includes(blogPost.id),
          'BlogPostListViewItem--highlighted':
            props.blogPostsHighlight.itemId === blogPost.id,
        }}
        blogPost={blogPost}
        selectionUIProps={selectionUIConnector.handle(blogPost.id)}
      />
    ));

    return (
      <KeyboardEventHandler
        handleKeys={R.keys(keyHandlers)}
        onKeyEvent={createKeyDownHandler(keyHandlers)}
      >
        <div className="BlogPostListView" tabIndex={1}>
          {blogPostDivs}
        </div>
      </KeyboardEventHandler>
    );
  }, ContextProps)
);
