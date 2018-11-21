import React from 'react';

class ExampleWork extends React.Component {
  render() {
    return (

      <div className="background--nightsky">
        <section className="section section--alignCentered section--description">
          <ExampleWorkBubble />

          <div className="section__exampleWrapper">
            <div className="section__example">
              <img alt="example screenshot of a project involving cats"
                   className="section__exampleImage"
                   src="images/resume.PNG"/>
              <dl className="color--cloud">
                <dt className="section__exampleTitle section__text--centered">
                  Resume
                </dt>
                <dd></dd>
              </dl>
            </div>
          </div>

          <div className="section__exampleWrapper">
            <div className="section__example">
              <img alt="example screenshot of a project involving cats"
                   className="section__exampleImage"
                   src="images/graduation.jpg"/>
              <dl className="color--cloud">
                <dt className="section__exampleTitle section__text--centered">
                  Certifications
                </dt>
                <dd></dd>
              </dl>
            </div>
          </div>
        </section>
      </div>

    )
  }
}

class ExampleWorkBubble extends React.Component {
  render() {
    return (
      <div className="section__exampleWrapper">
        <div className="section__example">
          <img alt="A Serverless Portfolio"
               className="section__exampleImage"
               src="images/serverlessportfolio.PNG"/>
          <dl className="color--cloud">
            <dt className="section__exampleTitle section__text--centered ">
              Serverless Portfolio
            </dt>
            <dd></dd>
          </dl>
        </div>
      </div>
    )
  }

}

export default ExampleWork;
