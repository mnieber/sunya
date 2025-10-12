import { observer } from 'mobx-react-lite';
import ReactMarkdown from 'react-markdown';
import { MilestoneT } from '/src/api/types';
import { cn } from '/src/utils/classnames';

import './MilestoneView.scss';

export type PropsT = {
  milestone: MilestoneT;
  className?: any;
};

export const MilestoneView = observer((props: PropsT) => {
  return (
    <div className={cn('MilestoneView', props.className)}>
      <div className="MilestoneView__header">
        <h2 className="MilestoneView__title">{props.milestone.title}</h2>
      </div>
      <div className="MilestoneView__content">
        <ReactMarkdown>{props.milestone.markdownContent}</ReactMarkdown>
      </div>
    </div>
  );
});
