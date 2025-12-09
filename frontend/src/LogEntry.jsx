import { useState, useEffect } from 'react'

import "bootstrap/dist/css/bootstrap.min.css";

export function LogEntry(props) {
	return (
		<div className='log-entry'>
			<p>{props.url}</p>
			<button
				onClick={() => {props.parentHandleClick(props.url)}}
			>
				Show
			</button>
		</div>
	);
}