CREATE TABLE "users" (
  "id" int PRIMARY KEY,
  "first_name" varchar(25) NOT NULL,
  "last_name" varchar(25) NOT NULL,
  "email" varchar(200) NOT NULL,
  "password" varchar(35) NOT NULL,
  "img" url
);

CREATE TABLE "post" (
  "id" int PRIMARY KEY,
  "meal_id" integer NOT NULL,
  "user_id" integer NOT NULL,
  "post" text NOT NULL,
  "time" timestamp
);

CREATE TABLE "comment" (
  "id" int PRIMARY KEY,
  "user_id" integer NOT NULL,
  "post_id" integer NOT NULL,
  "comment" text NOT NULL,
  "time" timestamp
);

CREATE TABLE "favorites" (
  "id" int PRIMARY KEY,
  "meal_id" int NOT NULL,
  "user_id" int NOT NULL
);

ALTER TABLE "post" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "comment" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "post" ADD FOREIGN KEY ("id") REFERENCES "comment" ("post_id");

ALTER TABLE "favorites" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
