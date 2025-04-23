package com.example.product_crud_assignment;

   import lombok.Getter;
   import lombok.Setter;

   @Getter
   @Setter
   public class Product {
       private String id;
       private String name;
       private String description;
       private double price;
       private int quantity;

       public Product(String id, String name, String description, double price, int quantity) {
           this.id = id;
           this.name = name;
           this.description = description;
           this.price = price;
           this.quantity = quantity;
       }
   }