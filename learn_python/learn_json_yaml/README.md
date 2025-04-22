# Comparing JSON and YAML

JSON:
```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Python", "DevOps"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}
```
- courses are a list [], address is more like a dictionary {key: value}
- commas to separate
- all values need quotes 

YAML:
```yaml
name: John Doe
age: 30
isStudent: false
courses:
  - Python
  - DevOps
address:
  street: 123 Main St
  city: Anytown
```

- lists are dashed lists
- dictionary doesn't need quotes around the values
- key, value pairs are indented
