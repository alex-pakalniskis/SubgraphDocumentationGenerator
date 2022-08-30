mod structs;
mod utilities;

use std::fs;
use reqwest::Error;
use crate::structs::SubgraphParameters;
use crate::utilities::prepare_ipfs_url;

#[tokio::main]
async fn main() -> Result<(), Error> {

    let mut subgraph_parameters = SubgraphParameters {
        name: String::from("Everest"),
        manifest_id: String::from("QmVsp1bC9rS3rf861cXgyvsqkpdsTXKSnS4729boXZvZyH"),
        github: String::from("https://github.com/graphprotocol/everest"),
        queries_http: String::from("https://api.thegraph.com/subgraphs/name/graphprotocol/everest"),
    };
    
    let manifest_link = prepare_ipfs_url(&subgraph_parameters.manifest_id);
    let manifest_response = reqwest::get(&manifest_link).await?;
    let manifest_text = manifest_response.text().await?;
    fs::write("./subgraph.yml", manifest_text).expect("Unable to save manifest data to file");

    // parse manifest for necessary data

    // download schema
    // let schema_link = prepare_ipfs_url(&manifest_data.schema_hash)

    // parse schema for entities

    // generate overview markdown

    // generate entities markdown

    // generate queries markdown

    Ok(())
}