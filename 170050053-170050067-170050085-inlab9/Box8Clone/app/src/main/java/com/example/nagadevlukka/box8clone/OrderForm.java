package com.example.nagadevlukka.box8clone;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class OrderForm extends AppCompatActivity {
     public Button sendButton;
    public void init(){
        sendButton=(Button)findViewById(R.id.sendButton);
        sendButton.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){
                Intent toy=new Intent(OrderForm.this,OrderReview.this);
                startActivity(toy);

            }
        };
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order_form);
        View v=findViewById(R.id.sendButton);
        v.setOnClickListener(this);
       init();
    }
}
