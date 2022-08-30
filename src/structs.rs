pub struct SubgraphParameters {
    pub name: String,
    pub manifest_id: String,
    pub github: String,
    pub queries_http: String,
}

pub struct Entity {
    pub name: String,
    pub type_of: String,
    pub description: String,
}

pub struct Schema {
    pub hash: String,
    pub contents: String,
    pub entities: Vec<Entity>,
}

pub struct Network {
    pub name: String,
    pub address: String,
    pub block_number: i32
}

pub struct Manifest {
    pub hash: String,
    pub contents: String,
    pub schema_hash: String,
    pub networks: Vec<Network>,
    pub description: String,
    pub repository: String,
}