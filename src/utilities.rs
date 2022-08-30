use reqwest::Error;

pub fn prepare_ipfs_url(hash: &String) -> String {
    let target = format!("https://ipfs.io/ipfs/{}", hash);
    return target;
}

pub fn parse_manifest_text(text: &String) {}