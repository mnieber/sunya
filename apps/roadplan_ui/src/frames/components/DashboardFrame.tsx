import React from 'react';
import { Ribbon } from '/src/ribbon/components/Ribbon';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './DashboardFrame.scss';

type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

export const DashboardFrame = (props: PropsT) => {
  return (
    <div className={cn('DashboardFrame', L.col.banner(), props.className)}>
      <Ribbon />
      {props.children}
    </div>
  );
};

export const DashboardFrameS = {};
