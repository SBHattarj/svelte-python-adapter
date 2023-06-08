<script lang="ts">
    import { browser } from "$app/environment";
    // import {parse, createVisitor} from "python-ast";
    if(!browser) (async () => {
        const {parse, createVisitor, walk} = await import("python-ast");
        console.log("hello")
        walk({
            enterAtom(ctx) {
                console.log(ctx.text)
            }
        }, parse(`
a = "b"
a = "c"
a += "d"
`));

    })()

</script>
<h1>Welcome to your library project</h1>
<p>Create your package using @sveltejs/package and preview/showcase your work with SvelteKit</p>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
