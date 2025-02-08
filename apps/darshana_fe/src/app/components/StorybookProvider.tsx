import { QueryClientProvider } from '@tanstack/react-query';
import { queryClient } from '/src/api/queryClient';

export type PropsT = React.PropsWithChildren<{}>;

export const StorybookProvider = (props: PropsT) => {
  return (
    <QueryClientProvider client={queryClient}>
      {props.children}
    </QueryClientProvider>
  );
};
