import classnames from 'classnames';
import { observer } from 'mobx-react-lite';
import { isUpdating } from 'mobx-resource-states';
import React from 'react';
import { selectionUIHandlers, SelectionUIPropsT } from 'skandha-facets';
import './BlogPostListViewItem.scss';
import { BlogPostT } from '/src/api/types';

export type PropsT = {
  blogPost: BlogPostT;
  className?: any;
  selectionUIProps: SelectionUIPropsT;
};

export const BlogPostListViewItem: React.FC<PropsT> = observer(
  (props: PropsT) => {
    return (
      <div
        className={classnames(
          'BlogPostListViewItem',
          { 'animate-delete': isUpdating(props.blogPost) },
          props.className
        )}
        {...selectionUIHandlers(props.selectionUIProps)}
      >
        {props.blogPost.title}
        {props.blogPost.isPublished ? ' ✔️' : ''}
      </div>
    );
  }
);
