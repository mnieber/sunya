import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { jiraNav } from '/src/jira/routes';
import { ToolButton } from '/src/frames/components/ToolButton';
import { ModestToolButtonTrim } from '/src/frames/components/ToolButton';
import { navTo } from '/src/routes/navHandler';

export type PropsT = {
  className?: any;
};

const ContextProps = {};

export const SyncAtlasWithJiraButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <ToolButton
        className={props.className}
        trim={ModestToolButtonTrim}
        iconName="repeat"
        label="Sync with Jira"
        onClick={() => navTo(jiraNav.syncAtlasWithJira({}))}
      />
    );
  }, ContextProps)
);
