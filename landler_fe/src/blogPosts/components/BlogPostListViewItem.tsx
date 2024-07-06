import classnames from 'classnames';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { selectionUIHandlers, SelectionUIPropsT } from 'skandha-facets';
import './BlogPostListViewItem.scss';
import { BlogPostT } from '/src/api/types';
import { isUpdating } from '/src/resourceStates/getState';

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
        {props.blogPost.name}
        {props.blogPost.state === 'done' ? ' ✔️' : ''}
      </div>
    );
  }
);
