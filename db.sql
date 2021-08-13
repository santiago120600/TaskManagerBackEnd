CREATE DATABASE IF NOT EXISTS taskmanager;
USE taskmanager;

CREATE TABLE user(
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    email_user VARCHAR(80),
    password_user VARCHAR(80),
    name_user VARCHAR(80)
);

CREATE TABLE folder(
    id_folder INT PRIMARY KEY AUTO_INCREMENT,
    name_folder VARCHAR(80),
    desc_folder TEXT
);

CREATE TABLE task(
    id_task INT PRIMARY KEY AUTO_INCREMENT,
    img_task VARCHAR(150),
    desc_task TEXT,
    completed BOOLEAN,
    user_id INT,
    folder_id INT,
    FOREIGN KEY(user_id) REFERENCES user(id_user),
    FOREIGN KEY(folder_id) REFERENCES folder(id_folder)
);

CREATE TABLE sub_task(
    id_sub_task INT PRIMARY KEY AUTO_INCREMENT,
    desc_sub_task TEXT,
    completed BOOLEAN,
    task_id INT,
    FOREIGN KEY(task_id) REFERENCES task(id_task)
);
