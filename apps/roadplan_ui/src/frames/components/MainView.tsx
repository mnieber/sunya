import { cn } from '/src/utils/classnames';

export type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

export const MainView = (props: PropsT) => {
  return (
    <div className={cn('MainView', 'min-h-0', props.className)}>
      {props.children}
    </div>
  );
};
