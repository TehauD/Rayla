const DB='rayla-lab', STORE='projects';
export async function openDB(){return await new Promise((ok,no)=>{const r=indexedDB.open(DB,1);r.onupgradeneeded=()=>r.result.createObjectStore(STORE,{keyPath:'id'});r.onsuccess=()=>ok(r.result);r.onerror=()=>no(r.error)})}
export async function saveProject(p){const db=await openDB();return await new Promise((ok,no)=>{const r=db.transaction(STORE,'readwrite').objectStore(STORE).put(p);r.onsuccess=()=>ok(p);r.onerror=()=>no(r.error)})}
export async function listProjects(){const db=await openDB();return await new Promise((ok,no)=>{const r=db.transaction(STORE).objectStore(STORE).getAll();r.onsuccess=()=>ok(r.result.sort((a,b)=>b.updated.localeCompare(a.updated)));r.onerror=()=>no(r.error)})}
export async function getProject(id){const db=await openDB();return await new Promise((ok,no)=>{const r=db.transaction(STORE).objectStore(STORE).get(id);r.onsuccess=()=>ok(r.result);r.onerror=()=>no(r.error)})}
export async function deleteProject(id){const db=await openDB();return await new Promise((ok,no)=>{const r=db.transaction(STORE,'readwrite').objectStore(STORE).delete(id);r.onsuccess=()=>ok();r.onerror=()=>no(r.error)})}
