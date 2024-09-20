import { z } from 'zod';
import { useObservableMutation } from '/src/api/lib/ObservableMutation';
import { invalidateGetProject } from '/src/api/queries/useGetProject';
import { post } from '/src/api/restClient';
import { ProjectT } from '/src/api/types/ProjectT';
import { parseResponse } from '/src/api/utils/parseResponse';
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
    formData.append(`files[${index}]`, file);
  });

  return post(url, formData)
    .then((response) => {
      const schema = z.object({});
      const res = parseResponse(schema, response.data);

      return waitOnDev(1000, res);
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
