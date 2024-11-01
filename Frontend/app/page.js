"use client";
import { generateSlug } from "@/libs/generateSlug";
import { Plus, Weight } from "lucide-react";
import React, { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import parse from "html-react-parser";
export default function Home() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [autoSlug, setSlug] = useState("");

  function handleTitle(e) {
    const newTitle = e.target.value;
    setTitle(newTitle);
    setSlug(generateSlug(newTitle));
  }
  async function handleSubmit(e) {
    e.preventDefault();
    const newBlog = {
      title,
      autoSlug,
      content,
    };
    console.log(newBlog);

  }

  const modules = {
    toolbar: [
      [{ header: [1, 2, 3, 4, false] }],
      ["bold", "italic", "underline", "strike", "blockquote"],
      [{ align: ["right", "", "center", "justify"] }],
      [{ list: "ordered" }, { list: "bullet" }],
      ["link", "color", "image"],
      [{ "code-block": true }],
      ["clean"],
    ],
  };

  const formats = [
    "header",
    "bold",
    "italic",
    "underline",
    "strike",
    "blockquote",
    "align",
    "list",
    "bullet",
    "link",
    "indent",
    "image",
    "code-block",
    "color",
  ];
  return (
    <div>
      <h2 className="text-4xl text-center font-semibold py-4">
        Gestor de contenido
      </h2>
      <div className="grid grid-cols-1 lg:grid-cols-2 p-8 gap-4">
        <div className="w-full max-w-3xl p-5 my-6 bg-white border border-gray-200 rounded-lg shadow mx-auto">
          <h2 className="text-3xl font-bold border-b border-gray-400 pb-2 mb-5 ">
            Editor de entrada
          </h2>
          <form onSubmit={handleSubmit}>
            <div className="grid gap-4 sm:grid-cols-2 sm:gap-6">
              <div className="sm:col-span-2">
                <label htmlFor="title" className="block text-sm font-medium leading-6 text-gray-900 mb-2 ">
                  Título de entrada
                </label>
                <div className="mt-2">
                  <input onChange={handleTitle} type="text" value={title} name="title" id="title" autoComplete="given-name" className="block w-full rounded-md border-0 py-2 px-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-purple-600 sm:text-sm sm:leading-6" 
                  placeholder="Ingrese el título de la entrada"/>
                </div>
              </div>
                
              <div className="sm:col-span-2">
                <label htmlFor="content" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                  Contenido</label>
                <ReactQuill theme="snow" value={content} onChange={setContent} modules={modules} formats={formats}/>
              </div>
            </div>
            <button type="submit" className="inline-flex items-center px-5 py-2.5 mt-4 sm:mt-6 text-sm font-medium text-center text-white bg-purple-700 rounded-lg focus:ring-4 focus:ring-purple-200 dark:focus:ring-purple-900 hover:bg-purple-800">
              <Plus className="w-5 h-5 mr-2" />
              <span>Crear entrada</span>
            </button>
          </form>
        </div>

        <div className=" blog-view w-full max-w-3xl p-8 my-6 bg-white border border-gray-200 rounded-lg shadow mx-auto">
          <h2 className="text-3xl font-bold border-b border-gray-400 pb-2 mb-5 ">
            Vista previa</h2>
          <div className="grid gap-4 sm:grid-cols-2 sm:gap-6">
            
            <div className="sm:col-span-full">
              {parse(content)}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}