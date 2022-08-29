// import fetch from 'node-fetch';

interface Inputs {
    github_url: string;
    id: string;
    queries_http: string;
}

interface Manifest {
    ipsh_hash: Inputs["id"];
    schema_ipfs_hash: string;
    networks: Network[];
    repository?: Inputs["github_url"];
    description?: string;
};

interface Network {
    name: string;
    address: string;
    start_block: number;
};

interface Schema {
    ipfs_hash: Manifest["schema_ipfs_hash"];
    entities: Entity[]
};

interface Entity {
    fields: Field[];
};

interface Field {
    name: string;
    type: string;
    description?: string;
};




// Get Manifest

// Parse Manifest for Schema Hash, Networks, and Description

// Get Schema

// Parse Schema Entities

// Generate Overview page

// Generate Schema Entities page

// Generate Sample Queries page

async function app() {
    // run all the stuff
};
