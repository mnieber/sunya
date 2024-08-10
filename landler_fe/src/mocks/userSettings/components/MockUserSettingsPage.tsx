import { observer } from 'mobx-react-lite';
import React from 'react';
import { L } from '/src/frames/layout';
import { cn } from '/src/utils/classnames';

// Import styles
import './MockUserSettingsPage.scss';

export type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

export const MockUserSettingsPage = observer((props: PropsT) => {
  return (
    <div className={cn('MockUserSettingsPage', L.row.bar(), props.className)}>
      <h1>User Settings</h1>
    </div>
  );
});
