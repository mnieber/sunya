import { observer } from 'mobx-react-lite';
import { FormStateProvider } from 'react-form-state-context';
import { withContextProps } from 'react-props-from-context';
import { form } from './form';
import { blogPostsCtx } from '/src/blogPosts/hooks/useBlogPostsContext';
import {
  Field,
  FormCancelButton,
  FormFieldLabel,
  FormSaveButton,
  GlobalError,
  MarkdownField,
  NameField,
  SlugField,
} from '/src/forms/components';
import { usePreviewButton } from '/src/forms/hooks/usePreviewButton';
import { CardS } from '/src/frames/components/Card';
import { MainFormS } from '/src/frames/components/MainForm';
import { cn } from '/src/utils/classnames';

// Import styles
import './BlogPostFormView.scss';

export type PropsT = {
  className?: any;
};

export const ContextProps = {
  blogPost: blogPostsCtx.blogPost,
  blogPostsEdit: blogPostsCtx.blogPostsEdit,
};

export const BlogPostFormView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const { showPreviewButton, preview } = usePreviewButton({
      tabIndex: 9,
      className: 'font-normal',
    });

    if (!props.blogPost) {
      return null;
    }

    const initialValues = form.getInitialValues(props);
    const initialErrors = form.getInitialErrors(props);

    return (
      //
      // 🔳 BlogPostFormView 🔳
      //
      <div
        className={cn(CardS.root(), 'BlogPostFormView', [
          CardS.color.gray(),
          MainFormS.root.padding.default(),
          props.className,
        ])}
      >
        {
          // 🔳 FormStateProvider 🔳
        }
        <FormStateProvider
          initialValues={initialValues}
          initialErrors={initialErrors}
          handleValidate={form.getHandleValidate(props)}
          handleSubmit={form.getHandleSubmit(
            props,
            initialValues,
            initialErrors
          )}
          handleCancel={form.getHandleCancel(props)}
        >
          {
            // 🔳 Global error 🔳
          }
          <GlobalError className={MainFormS.GlobalError()} />
          {
            // 🔳 TitleField 🔳
          }
          <Field fieldName="blogPostForm.title" className={MainFormS.Field()}>
            <FormFieldLabel label="TITLE" />
            <NameField
              tabIndex={2}
              controlled={true}
              autoSelect={true}
              slugFieldName={
                initialValues['blogPostForm.slug'] === 'new-blog-post'
                  ? 'blogPostForm.slug'
                  : undefined
              }
            />
          </Field>
          {
            // 🔳 SlugField 🔳
          }
          <Field fieldName="blogPostForm.slug" className={MainFormS.Field()}>
            <FormFieldLabel label="SLUG" />
            <SlugField relatedFieldName="blogPostForm.title" />
          </Field>
          {
            // 🔳 ContentField 🔳
          }
          <Field
            fieldName="blogPostForm.content"
            tabOnEnter={false}
            className={MainFormS.Field()}
          >
            <FormFieldLabel label="CONTENT" buttons={[showPreviewButton]} />
            <MarkdownField tabIndex={6} controlled={true} preview={preview} />
          </Field>
          {
            // 🔳 Buttons 🔳
          }
          <div className={cn(MainFormS.Buttons())}>
            <FormCancelButton
              theme="MainView"
              className={cn(MainFormS.Button.root(), MainFormS.Button.gap())}
              tabIndex={10}
              label="Cancel"
            />
            <FormSaveButton
              theme="MainView"
              tabIndex={10}
              label="Save"
              className={cn(MainFormS.Button.root())}
            />
          </div>
        </FormStateProvider>
      </div>
    );
  }, ContextProps)
);
