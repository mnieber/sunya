import { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { useFormStateContext } from 'react-form-state-context';
import { useFormFieldContext } from '/src/forms/components';
import { cn } from '/src/utils/classnames';

// Import styles
import './FileUploadFormField.scss';

export type PropsT = {
  className?: any;
  accept?: Record<string, string[]>;
  multiple?: boolean;
};

export const FileUploadFormField = (props: PropsT) => {
  const formState = useFormStateContext();
  const fieldContext = useFormFieldContext();

  const onDrop = useCallback(
    (acceptedFiles: File[]) => {
      formState.setValue(fieldContext.fieldName, acceptedFiles);
    },
    [formState, fieldContext.fieldName]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: props.accept,
    multiple: props.multiple,
  });

  const files = formState.getValue(fieldContext.fieldName) || [];

  const handleDeleteFile = (indexToDelete: number) => {
    const updatedFiles = files.filter(
      (_: any, index: number) => index !== indexToDelete
    );
    formState.setValue(fieldContext.fieldName, updatedFiles);
  };

  return (
    <div className={cn('FileUploadFormField', props.className)}>
      <div
        {...getRootProps()}
        className={cn(
          'FileUploadFormField__DropZone',
          'cursor-pointer rounded-lg border-2 border-dashed border-gray-300 p-4 text-center',
          isDragActive ? 'border-blue-500 bg-blue-50' : 'hover:border-gray-400'
        )}
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <p>Drop the files here ...</p>
        ) : (
          <p>Drag 'n' drop some files here, or click to select files</p>
        )}
      </div>
      {files.length > 0 && (
        <ul className="FileUploadFormField__FileList mt-4">
          {files.map((file: File, index: number) => (
            <li key={index} className="mt-2 flex items-center justify-between">
              <span>{file.name}</span>
              <button
                onClick={() => handleDeleteFile(index)}
                className="text-red-500 hover:text-red-700"
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
