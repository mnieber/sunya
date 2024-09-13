import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProject } from '/src/api/queries/useGetProject';
import { post } from '/src/api/restClient';
import { ProjectT } from '/src/api/types/ProjectT';
import { ObjT } from '/src/utils/types';
import { waitOnDev } from '/src/utils/wait';

export type ImportSpecFilesArgsT = {
  project: ProjectT;
  files: File[];
};

export const importSpecFiles = (args: ImportSpecFilesArgsT) => {
  const url = `/projects/${args.project.id}/import-spec-files/`;
  const formData = new FormData();
  args.files.forEach((file, index) => {
    formData.append(`file${index}`, file);
  });

  return post(url, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })
    .then((response) => {
      return waitOnDev(1000, response);
    })
    .catch((error) => {
      // Handle specific error codes if needed
      throw error;
    });
};

export const useImportSpecFiles = () => {
  return useObservableMutation({
    mutationFn: importSpecFiles,
    onSuccess: (response: ObjT, args: ImportSpecFilesArgsT) => {
      invalidateGetProject({ projectId: args.project.id });
    },
  });
};
