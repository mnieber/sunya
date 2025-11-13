import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  className?: any;
};

const ContextProps = {};

export const SyncAtlasWithJiraView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <div className={cn('SyncAtlasWithJiraView', 'p-4', props.className)}>
        Sync Atlas with Jira (placeholder)
      </div>
    );
  }, ContextProps)
);
