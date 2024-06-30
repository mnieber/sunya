import { observer } from 'mobx-react-lite';
import { isLoading } from 'mobx-resource-states';
import { withContextProps } from 'react-props-from-context';
import { HighlightUIConnector } from 'skandha-facets';
import { LoaderBar } from '/src/frames/components/LoaderBar';
import { L } from '/src/frames/layout';
import { StepListViewKeyHandler } from '/src/steps/components';
import { StepListViewItem } from '/src/steps/components/StepListViewItem';
import { stepsCtx } from '/src/steps/hooks/useStepsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './StepListView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  steps: stepsCtx.steps,
  stepsHighlight: stepsCtx.stepsHighlight,
};

export const StepListView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    //
    // 🔳  Handle loading state 🔳
    //
    if (isLoading(props.steps)) {
      return <StepListViewLoader {...props} />;
    }

    const highlightUIConnector = new HighlightUIConnector({
      highlight: props.stepsHighlight,
    });

    //
    // 🔳 stepDivs 🔳
    //
    const stepDivs = props.steps.map((step) => {
      return (
        <StepListViewItem
          key={`item-${step.id}`}
          step={step}
          highlightUIProps={highlightUIConnector.handle(step.id)}
        />
      );
    });

    const noItems = <div>There are no steps</div>;

    //
    // 🔳 StepListView 🔳
    //
    return (
      <StepListViewKeyHandler>
        <div
          className={cn('StepListView', [L.col.banner(), props.className])}
          tabIndex={0}
        >
          {stepDivs.length > 0 && stepDivs}
          {stepDivs.length === 0 && noItems}
        </div>
      </StepListViewKeyHandler>
    );
  }, ContextProps)
);

export const StepListViewLoader = (props: { className?: any }) => {
  const loaderBars = ['1', '2', '3'].map((id: string) => {
    return <LoaderBar key={`item-${id}`} className={cn('my-4 h-6')} />;
  });

  return (
    <div
      className={cn('StepListViewLoader', [L.col.banner(), props.className])}
    >
      {loaderBars}
    </div>
  );
};
