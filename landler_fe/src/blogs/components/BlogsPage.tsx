import React from 'react';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './BlogsPage.scss';

type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

export const BlogsPage = (props: PropsT) => {
  return (
    <div className={cn('BlogsPage', L.col.skewer(), props.className)}>
      {props.children}
    </div>
  );
};

export const BlogsPageS = {};
