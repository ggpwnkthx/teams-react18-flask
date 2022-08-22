import { useContext } from "react";
import { Button, Loader } from "@fluentui/react-northstar";
import { useData } from "@microsoft/teamsfx-react";
import * as axios from "axios";
import { BearerTokenAuthProvider, createApiClient, TeamsFx } from "@microsoft/teamsfx";
import { TeamsFxContext } from "../Context";
import { JsonApiClient } from "../../libs/createJsonApiClient";

const functionName = process.env.REACT_APP_FUNC_NAME || "myFunc";

export function AzureFunctions(props: { codePath?: string; docsUrl?: string }) {
  const { codePath, docsUrl } = {
    codePath: `api/${functionName}/index.ts`,
    docsUrl: "https://aka.ms/teamsfx-azure-functions",
    ...props,
  };
  const teamsfx = useContext(TeamsFxContext).teamsfx;
  const client = new JsonApiClient({
    url: (teamsfx as TeamsFx).getConfig("apiEndpoint") + functionName,
    teamsfx: teamsfx
  })
  const { loading, data, error, reload } = useData(async () => client.fetch(["locations"]), {
    autoLoad: false,
  });
  return (
    <div>
      <h2>Call your Azure Function</h2>
      <p>An Azure Functions app is running. Authorize this app and click below to call it for a response:</p>
      <Button primary content="Call Azure Function" disabled={loading} onClick={reload} />
      {loading && (
        <pre className="fixed">
          {" "}
          <Loader />{" "}
        </pre>
      )}
      {!loading && !!data && !error && <pre className="fixed">{JSON.stringify(data.data, null, 2)}</pre>}
      {!loading && !data && !error && <pre className="fixed"></pre>}
      {!loading && !!error && <div className="error fixed">{(error as any).toString()}</div>}
      <h4>How to edit the Azure Function</h4>
      <p>
        See the code in <code>{codePath}</code> to add your business logic.
      </p>
      {!!docsUrl && (
        <p>
          For more information, see the{" "}
          <a href={docsUrl} target="_blank" rel="noreferrer">
            docs
          </a>
          .
        </p>
      )}
    </div>
  );
}
