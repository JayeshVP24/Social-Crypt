import Header from "@/components/Header";
import Head from "next/head";
import Image from "next/image";
import { FormEvent } from "react";

export default function Home() {
  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log(e.currentTarget["URL"].value);
  };

  return (
    <>
      <Head>
        <title>Social Crypt</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <main className="w-[100vw] px-10 lg:px-20">
        <section
          id="input"
          className="py-10 flex flex-col gap-10 lg:flex-row lg:justify-around lg:items-center"
        >
          <div className="lg:w-2/5">
            <Image
              alt="Hero Illustration"
              src="/hero.png"
              width="550"
              height="450"
              className="w-full max-w-[55rem] mx-auto rounded-3xl"
            />
          </div>
          <div className="lg:w-2/5">
            <h1 className="text-3xl lg:text-5xl font-bold">Crypt Check an Article!</h1>
            <form className="mt-5 text-xl space-y-6" onSubmit={handleSubmit}>
              <span>
                <label>Enter Article URL</label>
                <input
                  type="text"
                  name="URL"
                  className="w-full outline-none border-2 border-blue-600 p-2 pl-4 rounded-xl mt-2 placeholder:text-sm
                focus:ring-4 ring-blue-400 ring-opacity-40 "
                  placeholder="https://example.com/some-article"
                />
              </span>

              <button
                className="w-full bg-blue-400 py-2 rounded-xl  
            hover:ring-4 ring-blue-400 ring-opacity-40
            active:scale-90 transition-all"
              >
                Submit
              </button>
            </form>
          </div>
        </section>

        <article className="py-10 flex flex-col  lg:flex-row lg:justify-around lg:items-center">

          <div className="lg:w-2/5" >
            <h1 className="text-5xl font-bold mb-2">About us</h1>
            <p className="text-lg">
              Nowadays, it can be difficult to tell the difference between
              credible information and misinformation online 🌐. To solve this
              problem, Social Crypt provides users with a solution that lets
              them discover the truth behind the articles they read 📰. This
              application analyzes articles and detects misleading/propaganda
              information, coordinated bot activity, sentiment of entities
              mentioned, Social Media Activity of the same information, Source
              Authenticity and a lot more.
            </p>
            <p className="text-lg">
              Social Crypt is the solution you need to remain informed and make
              informed decisions, whether {"you're"} a journalist, researcher, or
              simply concerned about the reliability of the information you
              consume ⚠️.
            </p>
          </div>
          <div className="lg:w-2/5">
            <Image
              alt="Hero Illustration"
              src="/hero2.png"
              width="550"
              height="450"
              className="w-full max-w-[55rem] mx-auto rounded-3xl"
            />
          </div>

        </article>



        <article className="py-10 flex flex-col  lg:flex-row lg:justify-around lg:items-center">

          <div className="lg:w-2/5">
            <Image
              alt="Hero Illustration"
              src="/hero3.png"
              width="550"
              height="450"
              className="w-full max-w-[55rem] mx-auto rounded-3xl"
            />
          </div>


          <div className="lg:w-2/5 space-y-2"  >
            <h1 className="text-5xl font-bold mb-2">Features</h1>
            <p className="text-base"> <span className="font-bold text-lg"> 📰 Sentiment Analysis </span>: Measures the sentiment of entities mentioned in articles, providing a balanced view of the information being presented.</p>
            <p> <span className="font-bold text-lg"> ⚠️ Unrevealing Misinformation:</span> Helping users identify unreliable sources by detecting and flagging misleading or inaccurate information.</p>
            <p> <span className="font-bold text-lg"> 🤖 Bot Activity Detection: </span> Identifies coordinated clusters of bots and automatons, providing insight into potential manipulation and disinformation campaigns.</p>
            <p> <span className="font-bold text-lg"> 📱 Social Media Presence: </span> Explores the presence of the same information present on the social media like twitter and other metadata associated with it like like, share, top user retweeting it the most, etc.</p>


          </div>
        </article>
      </main>
      <footer  className="w-full flex  bg-gray-800">
          <div className="w-2/4 h-full">

          </div>
          <div className="w-2/4 flex justify-center items-center">
            <div className="space-y-2">
              <p className="text-xl text-white">Created by-</p>
              <div className="space-x-2 flex items-center"><Image width="40"  height="40" src='/github.png'></Image><p className="text-lg text-white">jayesh Potlabattini</p></div>
              <div className="space-x-2 flex items-center"><Image width="40" height="40" src='/github.png'/><p className="text-lg text-white">Hrishikesh Yadav</p></div>
             <div className="space-x-2 flex items-center"><Image width="40" height="40" src='/github.png'/><p className="text-lg text-white">Prathik shetty</p></div>
              <div className="space-x-2 flex items-center"><Image width="40" height="40" src='/github.png'/><p className="text-lg text-white">Roshan Patil</p></div>
            </div>
          </div>
        </footer>
    </>
  );
}