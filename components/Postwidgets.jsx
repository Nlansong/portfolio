import React, { useEffect, useState } from 'react'
import moment from 'moment'
import Link from 'next/link'
import { getRecentPosts, getSimilarPosts} from '@/services';

function Postwidgets({categories, slug}) {
    const [relatedPosts, setRelatedPosts ] = useState([]);
    useEffect(() =>{
        if(slug) {
            getSimilarPosts(categories, slug)
            .then((result) => setRelatedPosts(result))
        } else{
            getRecentPosts()
            .then((result) => setRelatedPosts(result))
        }

    }, [slug])
    
  return (
    <div className="bg-black shadow-lg rounded-lg p-8 mb-8 text-white ">
        <h3 className='text-lg mb-8 font-semibold border-b pb-4'>
            {slug? 'Related Posts' : "Recent Posts"}
        </h3>
        {relatedPosts.map((post) =>(
            <div key={post.title} className="flex items-center w-full">
                <div className='w-16 flex-none'>
                    <img
                        alt={post.title}
                        height='60px'
                        width='60px'
                        className='align-middle rounded-full mb-8'
                        src={post.featuredImage.url}
                     />
                </div>
                <div className='flex-grow ml-4'>
                    <p className='font-xs text-gray-500'>
                        {moment(post.createdAt).format('MMM DD, YYYY')}
                    </p>
                    <Link href={`/post/${post.slug}`} key={post.title} className="text-med">
                        {post.title}
                    </Link>
                </div>
            </div>
        ))}
    </div>
  )
}

export default Postwidgets