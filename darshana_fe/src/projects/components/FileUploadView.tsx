import { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { cn } from '/src/utils/classnames';

type PropsT = {
  onFilesUploaded: (files: File[]) => void;
  className?: string;
};

export const FileUploadView = (props: PropsT) => {
  const onDrop = useCallback(
    (acceptedFiles: File[]) => {
      props.onFilesUploaded(acceptedFiles);
    },
    [props.onFilesUploaded]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/x-yaml': ['.yaml', '.yml'],
    },
  });

  return (
    <div
      {...getRootProps()}
      className={cn(
        'cursor-pointer rounded-lg border-2 border-dashed border-gray-300 p-4 text-center',
        isDragActive ? 'border-blue-500 bg-blue-50' : 'hover:border-gray-400',
        props.className
      )}
    >
      <input {...getInputProps()} />
      {isDragActive ? (
        <p>Drop the files here ...</p>
      ) : (
        <p>Drag 'n' drop some files here, or click to select files</p>
      )}
    </div>
  );
};
