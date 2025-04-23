package com.example.product_crud_assignment;

import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/products")
public class ProductController {

    private List<Product> products = new ArrayList<>();

    // Helper method to find the index of a product by ID
    private int getProductIndex(String id) {
        for (Product product : products) {
            if (product.getId().equals(id)) {
                return products.indexOf(product);
            }
        }
        // Not found
        return -1;
    }

    // Implement the method to add a new product
    @PostMapping
    public Product createProduct(@RequestBody Product product) {
        products.add(product);
        return product; // Return the added product
    }

    // Implement the method to get all products
    @GetMapping
    public List<Product> getAllProducts() {
        return products; // Return the list of products
    }

    // Implement the method to get a product by ID
    @GetMapping("/{id}")
    public Product getProductById(@PathVariable String id) {
        int index = getProductIndex(id);
        if (index != -1) {
            return products.get(index); // Return the found product
        }
        return null; // Return null if not found
    }

    // Implement the method to update a product
    @PutMapping("/{id}")
    public Product updateProduct(@PathVariable String id, @RequestBody Product updatedProduct) {
        int index = getProductIndex(id);
        if (index != -1) {
            products.set(index, updatedProduct); // Update the product
            return updatedProduct; // Return the updated product
        }
        return null; // Return null if not found
    }

    // Implement the method to delete a product
    @DeleteMapping("/{id}")
    public void deleteProduct(@PathVariable String id) {
        int index = getProductIndex(id);
        if (index != -1) {
            products.remove(index); // Remove the product
        }
    }
}